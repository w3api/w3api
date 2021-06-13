---
title: XAResource.getTransactionTimeout()
permalink: /Java/XAResource/getTransactionTimeout/
date: 2021-01-11
key: Java.X.XAResource
category: Java
tags: ['java se', 'javax.transaction.xa', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XAResource.metodos valor="getTransactionTimeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int getTransactionTimeout() throws XAException
~~~

## Excepciones
[XAException](/Java/XAException/)

## Clase Padre
[XAResource](/Java/XAResource/)

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
