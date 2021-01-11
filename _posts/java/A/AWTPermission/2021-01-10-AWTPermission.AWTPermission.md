---
title: AWTPermission.AWTPermission()
permalink: Java/AWTPermission/AWTPermission
date: 2021-01-10
key: JavaJava.A.AWTPermission
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AWTPermission.constructores valor="AWTPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AWTPermission(String name)
public AWTPermission(String name, String actions)
~~~

## Parámetros
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AWTPermission](/Java/AWTPermission/)

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
