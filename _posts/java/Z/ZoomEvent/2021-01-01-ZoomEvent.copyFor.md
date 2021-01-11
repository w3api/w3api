---
title: ZoomEvent.copyFor()
permalink: Java/ZoomEvent/copyFor
date: 2021-01-11
key: JavaJava.Z.ZoomEvent
category: java
tags: ['java se', 'javafx.scene.input', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoomEvent.metodos valor="copyFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZoomEvent copyFor(Object newSource, EventTarget newTarget, EventType<ZoomEvent> type)
~~~

## Parámetros
* **EventType&lt;ZoomEvent&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="EventType<ZoomEvent> type" %}
* **Object newSource**,  {% include w3api/param_description.html metodo=_dato parametro="Object newSource" %}
* **EventTarget newTarget**,  {% include w3api/param_description.html metodo=_dato parametro="EventTarget newTarget" %}

## Clase Padre
[ZoomEvent](/Java/ZoomEvent/)

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
