---
title: CheckboxMenuItem.getListeners()
permalink: /Java/CheckboxMenuItem/getListeners/
date: 2021-01-11
key: Java.C.CheckboxMenuItem
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CheckboxMenuItem.metodos valor="getListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends EventListener>T[] getListeners(Class<T> listenerType)
~~~

## Parámetros
* **Class&lt;T&gt; listenerType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> listenerType" %}

## Clase Padre
[CheckboxMenuItem](/Java/CheckboxMenuItem/)

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
