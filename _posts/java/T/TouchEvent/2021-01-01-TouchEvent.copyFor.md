---
title: TouchEvent.copyFor()
permalink: /Java/TouchEvent/copyFor/
date: 2021-01-11
key: Java.T.TouchEvent
category: Java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TouchEvent.metodos valor="copyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TouchEvent copyFor(Object newSource, EventTarget newTarget)
public TouchEvent copyFor(Object newSource, EventTarget newTarget, EventType<TouchEvent> type)
~~~

## Parámetros
* **EventType&lt;TouchEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<TouchEvent> type" %}
* **Object newSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object newSource" %}
* **EventTarget newTarget**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget newTarget" %}

## Clase Padre
[TouchEvent](/Java/TouchEvent/)

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
