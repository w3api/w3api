---
title: EventListenerList.getListeners()
permalink: /Java/EventListenerList/getListeners/
date: 2021-01-11
key: Java.E.EventListenerList
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventListenerList.metodos valor="getListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends EventListener>T[] getListeners(Class<T> t)
~~~

## Parámetros
* **Class&lt;T&gt; t**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> t" %}

## Clase Padre
[EventListenerList](/Java/EventListenerList/)

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
