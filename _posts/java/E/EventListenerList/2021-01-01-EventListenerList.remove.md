---
title: EventListenerList.remove()
permalink: /Java/EventListenerList/remove/
date: 2021-01-11
key: Java.E.EventListenerList
category: Java
tags: ['java se', 'javax.swing.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventListenerList.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends EventListener>void remove(Class<T> t, T l)
~~~

## Parámetros
* **T l**,  {% include w3api/param_description.html metodo=_dato parametro="T l" %}
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
