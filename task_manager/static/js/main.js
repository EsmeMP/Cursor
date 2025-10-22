// JavaScript para el Gestor de Tareas

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide alerts después de 5 segundos
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Confirmación para eliminar tareas
    const deleteButtons = document.querySelectorAll('a[href*="delete_task"]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro de que quieres eliminar esta tarea?')) {
                e.preventDefault();
            }
        });
    });

    // Confirmación para completar tareas
    const completeButtons = document.querySelectorAll('a[href*="complete_task"]');
    completeButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('¿Marcar esta tarea como completada?')) {
                e.preventDefault();
            }
        });
    });

    // Validación del formulario de nueva tarea
    const addTaskForm = document.querySelector('form[action*="add_task"]');
    if (addTaskForm) {
        addTaskForm.addEventListener('submit', function(e) {
            const title = document.getElementById('title').value.trim();
            if (!title) {
                e.preventDefault();
                alert('El título de la tarea es obligatorio');
                document.getElementById('title').focus();
            }
        });
    }

    // Validación del formulario de editar tarea
    const editTaskForm = document.querySelector('form[method="POST"]:not([action*="add_task"])');
    if (editTaskForm) {
        editTaskForm.addEventListener('submit', function(e) {
            const title = document.getElementById('title').value.trim();
            if (!title) {
                e.preventDefault();
                alert('El título de la tarea es obligatorio');
                document.getElementById('title').focus();
            }
        });
    }

    // Auto-focus en el campo título cuando se abre el modal
    const addTaskModal = document.getElementById('addTaskModal');
    if (addTaskModal) {
        addTaskModal.addEventListener('shown.bs.modal', function() {
            document.getElementById('title').focus();
        });
    }

    // Animación de entrada para las tarjetas
    const cards = document.querySelectorAll('.card');
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });

    cards.forEach(function(card) {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(card);
    });

    // Función para actualizar estadísticas (si se implementa AJAX en el futuro)
    function updateStats() {
        // Esta función se puede usar para actualizar estadísticas sin recargar la página
        console.log('Actualizando estadísticas...');
    }

    // Función para filtrar tareas (funcionalidad futura)
    function filterTasks(filter) {
        const cards = document.querySelectorAll('.card');
        cards.forEach(function(card) {
            if (filter === 'all') {
                card.style.display = 'block';
            } else {
                const priority = card.querySelector('.badge').textContent.toLowerCase();
                const status = card.querySelectorAll('.badge')[1].textContent.toLowerCase();
                
                if (filter === 'completed' && status === 'completada') {
                    card.style.display = 'block';
                } else if (filter === 'pending' && status === 'pendiente') {
                    card.style.display = 'block';
                } else if (filter === 'high' && priority === 'alta') {
                    card.style.display = 'block';
                } else if (filter !== 'all') {
                    card.style.display = 'none';
                }
            }
        });
    }

    // Exponer funciones globalmente para uso futuro
    window.taskManager = {
        updateStats: updateStats,
        filterTasks: filterTasks
    };
});
