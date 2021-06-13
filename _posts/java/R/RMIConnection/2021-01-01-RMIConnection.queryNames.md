---
title: RMIConnection.queryNames()
permalink: /Java/RMIConnection/queryNames/
date: 2021-01-11
key: Java.R.RMIConnection
category: Java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="queryNames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Set<ObjectName> queryNames(ObjectName name, MarshalledObject query, Subject delegationSubject) throws IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}
* **MarshalledObject query**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject query" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

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
