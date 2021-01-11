---
title: RMIConnection.addNotificationListener()
permalink: Java/RMIConnection/addNotificationListener
date: 2021-01-11
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="addNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addNotificationListener(ObjectName name, ObjectName listener, MarshalledObject filter, MarshalledObject handback, Subject delegationSubject) throws InstanceNotFoundException, IOException
~~~

## Parámetros
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject delegationSubject" %}
* **ObjectName listener**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName listener" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectName name" %}
* **MarshalledObject handback**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject handback" %}
* **MarshalledObject filter**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject filter" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/)

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
