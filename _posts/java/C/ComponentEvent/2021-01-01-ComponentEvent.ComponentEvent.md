---
title: ComponentEvent.ComponentEvent()
permalink: Java/ComponentEvent/ComponentEvent
date: 2021-01-11
key: JavaJava.C.ComponentEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentEvent.constructores valor="ComponentEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ComponentEvent(Component source, int id)
~~~

## Parámetros
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ComponentEvent](/Java/ComponentEvent/)

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
