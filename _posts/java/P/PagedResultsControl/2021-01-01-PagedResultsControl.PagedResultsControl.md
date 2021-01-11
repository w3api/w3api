---
title: PagedResultsControl.PagedResultsControl()
permalink: Java/PagedResultsControl/PagedResultsControl
date: 2021-01-11
key: JavaJava.P.PagedResultsControl
category: java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PagedResultsControl.constructores valor="PagedResultsControl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PagedResultsControl(int pageSize, boolean criticality) throws IOException
public PagedResultsControl(int pageSize, byte[] cookie, boolean criticality) throws IOException
~~~

## Parámetros
* **int pageSize**,  {% include w3api/param_description.html metodo=_dato parametro="int pageSize" %}
* **byte[] cookie**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] cookie" %}
* **boolean criticality**,  {% include w3api/param_description.html metodo=_dato parametro="boolean criticality" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[PagedResultsControl](/Java/PagedResultsControl/)

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
