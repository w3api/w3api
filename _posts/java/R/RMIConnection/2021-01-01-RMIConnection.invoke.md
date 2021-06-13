---
title: RMIConnection.invoke()
permalink: /Java/RMIConnection/invoke/
date: 2021-01-11
key: Java.R.RMIConnection
category: Java
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
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}
* **MarshalledObject params**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject params" %}
* **String[] signature**,  {% include w3api/param_description.html metodo=_dato parametro="String[] signature" %}
* **String operationName**,  {% include w3api/param_description.html metodo=_dato parametro="String operationName" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/), [ReflectionException](/Java/ReflectionException/), [SecurityException](/Java/SecurityException/), [MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/)

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
