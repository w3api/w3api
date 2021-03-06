---
title: WindowEvent.copyFor()
permalink: /Java/WindowEvent-javafx-stage/copyFor/
date: 2021-01-11
key: Java.W.WindowEvent-javafx-stage
category: Java
tags: ['java se', 'javafx.stage', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WindowEvent-javafx-stage.metodos valor="copyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WindowEvent copyFor(Object newSource, EventTarget newTarget, EventType<WindowEvent> type)
~~~

## Parámetros
* **EventType&lt;WindowEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<WindowEvent> type" %}
* **Object newSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object newSource" %}
* **EventTarget newTarget**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget newTarget" %}

## Clase Padre
[WindowEvent](/Java/WindowEvent-javafx-stage/)

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
