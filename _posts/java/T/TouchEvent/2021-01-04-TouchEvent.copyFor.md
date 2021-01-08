---
title: TouchEvent.copyFor()
permalink: Java/TouchEvent/copyFor
date: 2021-01-04
key: JavaJava.T.TouchEvent
category: java
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
* **Object newSource**,  {% include w3api/param_description.html metodo=_data parametro="Object newSource" %}
* **EventType&lt;TouchEvent&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="EventType<TouchEvent> type" %}
* **EventTarget newTarget**,  {% include w3api/param_description.html metodo=_data parametro="EventTarget newTarget" %}

## Clase Padre
[TouchEvent](/Java/TouchEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TouchEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
