---
title: BeanContextSupport.remove()
permalink: /Java/BeanContextSupport/remove/
date: 2021-01-11
key: JavaJava.B.BeanContextSupport
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextSupport.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean remove(Object targetChild)
protected boolean remove(Object targetChild, boolean callChildSetBC)
~~~

## Parámetros
* **boolean callChildSetBC**,  {% include w3api/param_description.html metodo=_dato parametro="boolean callChildSetBC" %}
* **Object targetChild**,  {% include w3api/param_description.html metodo=_dato parametro="Object targetChild" %}

## Clase Padre
[BeanContextSupport](/Java/BeanContextSupport/)

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
