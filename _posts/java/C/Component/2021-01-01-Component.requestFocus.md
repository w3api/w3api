---
title: Component.requestFocus()
permalink: Java/Component/requestFocus
date: 2021-01-11
key: JavaJava.C.Component
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="requestFocus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void requestFocus()
protected boolean requestFocus(boolean temporary)
protected boolean requestFocus(boolean temporary, FocusEvent.Cause cause)
public void requestFocus(FocusEvent.Cause cause)
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

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
