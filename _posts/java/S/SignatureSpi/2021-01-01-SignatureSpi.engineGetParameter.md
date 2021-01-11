---
title: SignatureSpi.engineGetParameter()
permalink: Java/SignatureSpi/engineGetParameter
date: 2021-01-11
key: JavaJava.S.SignatureSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignatureSpi.metodos valor="engineGetParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated protected abstract Object engineGetParameter(String param) throws InvalidParameterException
~~~

## Parámetros
* **String param**,  {% include w3api/param_description.html metodo=_dato parametro="String param" %}

## Excepciones
[InvalidParameterException](/Java/InvalidParameterException/)

## Clase Padre
[SignatureSpi](/Java/SignatureSpi/)

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
