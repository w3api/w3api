---
title: SecurityManager.checkTopLevelWindow()
permalink: Java/SecurityManager/checkTopLevelWindow
date: 2021-01-04
key: JavaJava.S.SecurityManager
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecurityManager.metodos valor="checkTopLevelWindow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="1.8", forRemoval=true) public boolean checkTopLevelWindow(Object window)
~~~

## Parámetros
* **Object window**,  {% include w3api/param_description.html metodo=_data parametro="Object window" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SecurityManager](/Java/SecurityManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecurityManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
