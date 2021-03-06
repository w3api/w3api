---
title: ContainerEvent.ContainerEvent()
permalink: /Java/ContainerEvent/ContainerEvent/
date: 2021-01-11
key: Java.C.ContainerEvent
category: Java
tags: ['java se', 'java.awt.event', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContainerEvent.constructores valor="ContainerEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ContainerEvent(Component source, int id, Component child)
~~~

## Parámetros
* **Component child**,  {% include w3api/param_description.html metodo=_dato parametro="Component child" %}
* **int id**,  {% include w3api/param_description.html metodo=_dato parametro="int id" %}
* **Component source**,  {% include w3api/param_description.html metodo=_dato parametro="Component source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ContainerEvent](/Java/ContainerEvent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
