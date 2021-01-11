---
title: WorkerStateEvent.WorkerStateEvent()
permalink: Java/WorkerStateEvent/WorkerStateEvent
date: 2021-01-11
key: JavaJava.W.WorkerStateEvent
category: java
tags: ['java se', 'javafx.concurrent', 'javafx.graphics', 'metodo java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WorkerStateEvent.constructores valor="WorkerStateEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WorkerStateEvent(Worker worker, EventType<? extends WorkerStateEvent> eventType)
~~~

## Parámetros
* **EventType&lt;? extends WorkerStateEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<? extends WorkerStateEvent> eventType" %}
* **Worker worker**,  {% include w3api/param_description.html metodo=_dato parametro="Worker worker" %}

## Clase Padre
[WorkerStateEvent](/Java/WorkerStateEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
