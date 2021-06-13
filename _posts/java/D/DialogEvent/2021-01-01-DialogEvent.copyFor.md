---
title: DialogEvent.copyFor()
permalink: /Java/DialogEvent/copyFor/
date: 2021-01-11
key: Java.D.DialogEvent
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DialogEvent.metodos valor="copyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DialogEvent copyFor(Object newSource, EventTarget newTarget, EventType<DialogEvent> type)
~~~

## Parámetros
* **EventType&lt;DialogEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<DialogEvent> type" %}
* **Object newSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object newSource" %}
* **EventTarget newTarget**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget newTarget" %}

## Clase Padre
[DialogEvent](/Java/DialogEvent/)

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
