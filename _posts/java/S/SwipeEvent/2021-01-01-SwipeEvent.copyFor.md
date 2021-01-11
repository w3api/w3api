---
title: SwipeEvent.copyFor()
permalink: Java/SwipeEvent/copyFor
date: 2021-01-11
key: JavaJava.S.SwipeEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SwipeEvent.metodos valor="copyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SwipeEvent copyFor(Object newSource, EventTarget newTarget, EventType<SwipeEvent> type)
~~~

## Parámetros
* **EventType&lt;SwipeEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<SwipeEvent> type" %}
* **Object newSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object newSource" %}
* **EventTarget newTarget**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget newTarget" %}

## Clase Padre
[SwipeEvent](/Java/SwipeEvent/)

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
