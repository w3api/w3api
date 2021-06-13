---
title: FocusEvent.FocusEvent()
permalink: /Java/FocusEvent/FocusEvent/
date: 2021-01-11
key: Java.F.FocusEvent
category: Java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FocusEvent.constructores valor="FocusEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FocusEvent(Component source, int id)
public FocusEvent(Component source, int id, boolean temporary)
public FocusEvent(Component source, int id, boolean temporary, Component opposite)
public FocusEvent(Component source, int id, boolean temporary, Component opposite, FocusEvent.Cause cause)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Component opposite**,  {% include w3api/param_description.html metodo=_dato parametro="Component opposite" %}
* **boolean temporary**,  {% include w3api/param_description.html metodo=_dato parametro="boolean temporary" %}
* **FocusEvent.Cause cause**,  {% include w3api/param_description.html metodo=_dato parametro="FocusEvent.Cause cause" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FocusEvent](/Java/FocusEvent/)

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
