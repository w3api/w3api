---
title: XAResource.forget()
permalink: /Java/XAResource/forget/
date: 2021-01-11
key: Java.X.XAResource
category: Java
tags: ['java se', 'javax.transaction.xa', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XAResource.metodos valor="forget" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void forget(Xid xid) throws XAException
~~~

## Parámetros
* **Xid xid**,  {% include w3api/param_description.html metodo=_dato parametro="Xid xid" %}

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
