---
title: Component.lostFocus()
permalink: /Java/Component/lostFocus/
date: 2021-01-11
key: Java.C.Component
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="lostFocus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public boolean lostFocus(Event evt, Object what)
~~~

## Parámetros
* **Event evt**,  {% include w3api/param_description.html metodo=_dato parametro="Event evt" %}
* **Object what**,  {% include w3api/param_description.html metodo=_dato parametro="Object what" %}

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
