import { Routes } from '@angular/router';
import { ProjectsComponent } from './pages/projects/projects';
import { TasksComponent } from './pages/tasks/tasks';

export const routes: Routes = [
    {
        path: '',
        component: ProjectsComponent
    },
    {
        path: 'tasks',
        component: TasksComponent
    }
];
