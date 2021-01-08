---
title: RMIConnection.invoke()
permalink: Java/RMIConnection/invoke
date: 2021-01-04
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object invoke(ObjectName name, String operationName, MarshalledObject params, String[] signature, Subject delegationSubject) throws InstanceNotFoundException, MBeanException, ReflectionException, IOException
~~~

## Parámetros
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_data parametro="Subject delegationSubject" %}
* **String operationName**,  {% include w3api/param_description.html metodo=_data parametro="String operationName" %}
* **String[] signature**,  {% include w3api/param_description.html metodo=_data parametro="String[] signature" %}
* **MarshalledObject params**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject params" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [ReflectionException](/Java/ReflectionException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/)

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
