---
title: RMIConnection.getAttributes()
permalink: Java/RMIConnection/getAttributes
date: 2021-01-11
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="getAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AttributeList getAttributes(ObjectName name, String[] attributes, Subject delegationSubject) throws InstanceNotFoundException, ReflectionException, IOException
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}
* **String[] attributes**,  {% include w3api/param_description.html metodo=_dato parametro="String[] attributes" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/), [ReflectionException](/Java/ReflectionException/), [SecurityException](/Java/SecurityException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

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
