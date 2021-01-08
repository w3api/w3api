---
title: EventListenerList.remove()
permalink: Java/EventListenerList/remove
date: 2021-01-04
key: JavaJava.E.EventListenerList
category: java
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
* **Class&lt;T&gt; t**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> t" %}
* **T l**,  {% include w3api/param_description.html metodo=_data parametro="T l" %}

## Clase Padre
[EventListenerList](/Java/EventListenerList/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventListenerList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
