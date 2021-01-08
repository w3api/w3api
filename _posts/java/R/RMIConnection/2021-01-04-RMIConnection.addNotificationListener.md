---
title: RMIConnection.addNotificationListener()
permalink: Java/RMIConnection/addNotificationListener
date: 2021-01-04
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
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_data parametro="Subject delegationSubject" %}
* **MarshalledObject filter**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject filter" %}
* **ObjectName listener**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName listener" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}
* **MarshalledObject handback**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject handback" %}

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

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
