---
title: XAResource.recover()
permalink: Java/XAResource/recover
date: 2021-01-04
key: JavaJava.X.XAResource
category: java
tags: ['java se', 'javax.transaction.xa', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XAResource.metodos valor="recover" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Xid[] recover(int flag) throws XAException
~~~

## Parámetros
* **int flag**,  {% include w3api/param_description.html metodo=_data parametro="int flag" %}

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
{%- for _ldc in site.data.Java.X.XAResource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
