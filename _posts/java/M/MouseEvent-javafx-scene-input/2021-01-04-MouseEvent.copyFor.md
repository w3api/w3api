---
title: MouseEvent.copyFor()
permalink: Java/MouseEvent-javafx-scene-input/copyFor
date: 2021-01-04
key: JavaJava.M.MouseEvent-javafx-scene-input
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MouseEvent-javafx-scene-input.metodos valor="copyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MouseEvent copyFor(Object newSource, EventTarget newTarget)
public MouseEvent copyFor(Object newSource, EventTarget newTarget, EventType<? extends MouseEvent> eventType)
~~~

## Parámetros
* **EventType&lt;? extends MouseEvent&gt; eventType**,  {% include w3api/param_description.html metodo=_data parametro="EventType<? extends MouseEvent> eventType" %}
* **Object newSource**,  {% include w3api/param_description.html metodo=_data parametro="Object newSource" %}
* **EventTarget newTarget**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget newTarget" %}

## Clase Padre
[MouseEvent](/Java/MouseEvent-javafx-scene-input/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MouseEvent-javafx-scene-input.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
