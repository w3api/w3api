---
title: SystemException.SystemException()
permalink: Java/SystemException/SystemException
date: 2021-01-04
key: JavaJava.S.SystemException
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SystemException.constructores valor="SystemException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected SystemException(String reason, int minor, CompletionStatus completed)
~~~

## Parámetros
* **int minor**,  {% include w3api/param_description.html metodo=_data parametro="int minor" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStatus completed" %}

## Clase Padre
[SystemException](/Java/SystemException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SystemException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
