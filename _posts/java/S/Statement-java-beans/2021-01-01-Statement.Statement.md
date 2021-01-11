---
title: Statement.Statement()
permalink: Java/Statement-java-beans/Statement
date: 2021-01-11
key: JavaJava.S.Statement-java-beans
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-beans.constructores valor="Statement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@ConstructorProperties({"target","methodName","arguments"}) public Statement(Object target, String methodName, Object[] arguments)
~~~

## Parámetros
* **Object[] arguments**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] arguments" %}
* **Object target**,  {% include w3api/param_description.html metodo=_dato parametro="Object target" %}
* **String methodName**,  {% include w3api/param_description.html metodo=_dato parametro="String methodName" %}

## Clase Padre
[Statement](/Java/Statement-java-beans/)

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
