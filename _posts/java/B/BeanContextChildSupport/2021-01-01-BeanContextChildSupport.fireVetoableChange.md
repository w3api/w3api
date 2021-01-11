---
title: BeanContextChildSupport.fireVetoableChange()
permalink: Java/BeanContextChildSupport/fireVetoableChange
date: 2021-01-11
key: JavaJava.B.BeanContextChildSupport
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextChildSupport.metodos valor="fireVetoableChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void fireVetoableChange(String name, Object oldValue, Object newValue) throws PropertyVetoException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}

## Excepciones
[PropertyVetoException](/Java/PropertyVetoException/)

## Clase Padre
[BeanContextChildSupport](/Java/BeanContextChildSupport/)

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