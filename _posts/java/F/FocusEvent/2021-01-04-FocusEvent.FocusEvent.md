---
title: FocusEvent.FocusEvent()
permalink: Java/FocusEvent/FocusEvent
date: 2021-01-04
key: JavaJava.F.FocusEvent
category: java
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
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **boolean temporary**,  {% include w3api/param_description.html metodo=_data parametro="boolean temporary" %}
* **Component source**,  {% include w3api/param_description.html metodo=_data parametro="Component source" %}
* **FocusEvent.Cause cause**,  {% include w3api/param_description.html metodo=_data parametro="FocusEvent.Cause cause" %}
* **Component opposite**,  {% include w3api/param_description.html metodo=_data parametro="Component opposite" %}

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
{%- for _ldc in site.data.Java.F.FocusEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
