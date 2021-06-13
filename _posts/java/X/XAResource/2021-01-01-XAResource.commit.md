---
title: XAResource.commit()
permalink: /Java/XAResource/commit/
date: 2021-01-11
key: Java.X.XAResource
category: Java
tags: ['java se', 'javax.transaction.xa', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XAResource.metodos valor="commit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void commit(Xid xid, boolean onePhase) throws XAException
~~~

## Parámetros
* **boolean onePhase**,  {% include w3api/param_description.html metodo=_dato parametro="boolean onePhase" %}
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
