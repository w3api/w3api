---
title: ObjectImpl._request()
permalink: /Java/ObjectImpl-org-omg-CORBA-portable/_request/
date: 2021-01-11
key: Java.O.ObjectImpl-org-omg-CORBA-portable
category: Java
tags: ['java se', 'org.omg.CORBA.portable', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectImpl-org-omg-CORBA-portable.metodos valor="_request" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Request _request(String operation)
public OutputStream _request(String operation, boolean responseExpected)
~~~

## Parámetros
* **String operation**,  {% include w3api/param_description.html metodo=_dato parametro="String operation" %}
* **boolean responseExpected**,  {% include w3api/param_description.html metodo=_dato parametro="boolean responseExpected" %}

## Clase Padre
[ObjectImpl](/Java/ObjectImpl-org-omg-CORBA-portable/)

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
