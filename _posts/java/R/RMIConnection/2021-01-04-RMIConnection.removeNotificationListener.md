---
title: RMIConnection.removeNotificationListener()
permalink: Java/RMIConnection/removeNotificationListener
date: 2021-01-04
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="removeNotificationListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void removeNotificationListener(ObjectName name, ObjectName listener, MarshalledObject filter, MarshalledObject handback, Subject delegationSubject) throws InstanceNotFoundException, ListenerNotFoundException, IOException
void removeNotificationListener(ObjectName name, ObjectName listener, Subject delegationSubject) throws InstanceNotFoundException, ListenerNotFoundException, IOException
~~~

## Parámetros
* **Subject delegationSubject**,  {% include w3api/param_description.html metodo=_data parametro="Subject delegationSubject" %}
* **MarshalledObject filter**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject filter" %}
* **ObjectName listener**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName listener" %}
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}
* **MarshalledObject handback**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject handback" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [ListenerNotFoundException](/Java/ListenerNotFoundException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [IOException](/Java/IOException/)

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
