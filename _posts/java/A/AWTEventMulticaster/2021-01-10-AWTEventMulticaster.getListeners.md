---
title: AWTEventMulticaster.getListeners()
permalink: Java/AWTEventMulticaster/getListeners
date: 2021-01-10
key: JavaJava.A.AWTEventMulticaster
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AWTEventMulticaster.metodos valor="getListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T extends EventListener>T[] getListeners(EventListener l, Class<T> listenerType)
~~~

## Parámetros
* **Class&lt;T&gt; listenerType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> listenerType" %}
* **EventListener l**,  {% include w3api/param_description.html metodo=_dato parametro="EventListener l" %}

## Clase Padre
[AWTEventMulticaster](/Java/AWTEventMulticaster/)

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
