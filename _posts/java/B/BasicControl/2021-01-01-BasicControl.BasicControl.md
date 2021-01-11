---
title: BasicControl.BasicControl()
permalink: Java/BasicControl/BasicControl
date: 2021-01-11
key: JavaJava.B.BasicControl
category: java
tags: ['java se', 'javax.naming.ldap', 'java.naming', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicControl.constructores valor="BasicControl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BasicControl(String id)
public BasicControl(String id, boolean criticality, byte[] value)
~~~

## Parámetros
* **boolean criticality**,  {% include w3api/param_description.html metodo=_dato parametro="boolean criticality" %}
* **byte[] value**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] value" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}

## Clase Padre
[BasicControl](/Java/BasicControl/)

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
