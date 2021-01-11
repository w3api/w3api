---
title: PKIXParameters.setCertPathCheckers()
permalink: Java/PKIXParameters/setCertPathCheckers
date: 2021-01-11
key: JavaJava.P.PKIXParameters
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKIXParameters.metodos valor="setCertPathCheckers" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setCertPathCheckers(List<PKIXCertPathChecker> checkers)
~~~

## Parámetros
* **List&lt;PKIXCertPathChecker&gt; checkers**,  {% include w3api/param_description.html metodo=_dato parametro="List<PKIXCertPathChecker> checkers" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/)

## Clase Padre
[PKIXParameters](/Java/PKIXParameters/)

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
