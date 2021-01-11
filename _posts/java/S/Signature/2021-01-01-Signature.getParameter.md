---
title: Signature.getParameter()
permalink: Java/Signature/getParameter
date: 2021-01-11
key: JavaJava.S.Signature
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Signature.metodos valor="getParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public final Object getParameter(String param) throws InvalidParameterException
~~~

## Parámetros
* **String param**,  {% include w3api/param_description.html metodo=_dato parametro="String param" %}

## Excepciones
[InvalidParameterException](/Java/InvalidParameterException/)

## Clase Padre
[Signature](/Java/Signature/)

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
