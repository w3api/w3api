---
title: RMIConnection.getAttribute()
permalink: Java/RMIConnection/getAttribute
date: 2021-01-11
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="getAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getAttribute(ObjectName name, String attribute, Subject delegationSubject) throws MBeanException, AttributeNotFoundException, InstanceNotFoundException, ReflectionException, IOException
~~~

## Parámetros
* **String attribute**,  {% include w3api/param_description.html metodo=_dato parametro="String attribute" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/), [ReflectionException](/Java/ReflectionException/), [SecurityException](/Java/SecurityException/), [AttributeNotFoundException](/Java/AttributeNotFoundException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeMBeanException](/Java/RuntimeMBeanException/)

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
