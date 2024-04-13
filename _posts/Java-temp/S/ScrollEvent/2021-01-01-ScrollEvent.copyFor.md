---
title: ScrollEvent.copyFor()
permalink: /Java/ScrollEvent/copyFor/
date: 2021-01-11
key: Java.S.ScrollEvent
category: Java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScrollEvent.metodos valor="copyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScrollEvent copyFor(Object newSource, EventTarget newTarget, EventType<ScrollEvent> type)
~~~

## Parámetros
* **EventType&lt;ScrollEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<ScrollEvent> type" %}
* **Object newSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object newSource" %}
* **EventTarget newTarget**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget newTarget" %}

## Clase Padre
[ScrollEvent](/Java/ScrollEvent/)

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
