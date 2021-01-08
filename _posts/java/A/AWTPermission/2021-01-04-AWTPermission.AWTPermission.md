---
title: AWTPermission.AWTPermission()
permalink: Java/AWTPermission/AWTPermission
date: 2021-01-04
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
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String actions**,  {% include w3api/param_description.html metodo=_data parametro="String actions" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AWTPermission](/Java/AWTPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AWTPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
