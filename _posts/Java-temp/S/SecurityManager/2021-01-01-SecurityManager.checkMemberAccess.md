---
title: SecurityManager.checkMemberAccess()
permalink: /Java/SecurityManager/checkMemberAccess/
date: 2021-01-11
key: Java.S.SecurityManager
category: Java
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
* **int which**,  {% include w3api/param_description.html metodo=_dato parametro="int which" %}
* **Class&lt;?&gt; clazz**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> clazz" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
