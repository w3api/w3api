---
title: ObjectImpl._request()
permalink: Java/ObjectImpl-org-omg-CORBA-portable/_request
date: 2021-01-04
key: JavaJava.O.ObjectImpl-org-omg-CORBA-portable
category: java
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
* **boolean responseExpected**,  {% include w3api/param_description.html metodo=_data parametro="boolean responseExpected" %}
* **String operation**,  {% include w3api/param_description.html metodo=_data parametro="String operation" %}

## Clase Padre
[ObjectImpl](/Java/ObjectImpl-org-omg-CORBA-portable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectImpl-org-omg-CORBA-portable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
