---
title: BeanContextSupport.getResourceAsStream()
permalink: /Java/BeanContextSupport/getResourceAsStream/
date: 2021-01-11
key: Java.B.BeanContextSupport
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextSupport.metodos valor="getResourceAsStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputStream getResourceAsStream(String name, BeanContextChild bcc)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **BeanContextChild bcc**,  {% include w3api/param_description.html metodo=_dato parametro="BeanContextChild bcc" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
