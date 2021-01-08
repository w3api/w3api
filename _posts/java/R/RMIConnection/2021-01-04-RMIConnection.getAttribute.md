---
title: RMIConnection.getAttribute()
permalink: Java/RMIConnection/getAttribute
date: 2021-01-04
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
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}
* **String attribute**,  {% include w3api/param_description.html metodo=_data parametro="String attribute" %}
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_data parametro="Subject delegationSubject" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [ReflectionException](/Java/ReflectionException/), [RuntimeMBeanException](/Java/RuntimeMBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [AttributeNotFoundException](/Java/AttributeNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
