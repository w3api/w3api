---
title: SecurityManager.checkMemberAccess()
permalink: Java/SecurityManager/checkMemberAccess
date: 2021-01-04
key: JavaJava.S.SecurityManager
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecurityManager.metodos valor="checkMemberAccess" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="1.8", forRemoval=true) public void checkMemberAccess(Class<?> clazz, int which)
~~~

## Parámetros
* **Class&lt;?&gt; clazz**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> clazz" %}
* **int which**,  {% include w3api/param_description.html metodo=_data parametro="int which" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

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
