---
title: Component.requestFocusInWindow()
permalink: /Java/Component/requestFocusInWindow/
date: 2021-01-11
key: Java.C.Component
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="requestFocusInWindow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean requestFocusInWindow()
protected boolean requestFocusInWindow(boolean temporary)
public boolean requestFocusInWindow(FocusEvent.Cause cause)
~~~

## Parámetros
* **boolean temporary**,  {% include w3api/param_description.html metodo=_dato parametro="boolean temporary" %}
* **FocusEvent.Cause cause**,  {% include w3api/param_description.html metodo=_dato parametro="FocusEvent.Cause cause" %}

## Clase Padre
[Component](/Java/Component/)

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
